import Text.Printf (printf)

differences :: [Int] -> [Int]
differences hist = zipWith subtract hist (tail hist)

predict :: Bool -> [Int] -> Int
predict past hist
  | all (== 0) hist = 0
  | past = head hist - predict past (differences hist)
  | otherwise = last hist + predict past (differences hist)

interpolate :: Bool -> [[Int]] -> Int
interpolate past = sum . map (predict past)

parseInput :: String -> [Int]
parseInput = map read . words

main :: IO ()
main = do
  input <- getContents
  let inp = map parseInput . lines $ input
  printf "%d %d\n" (interpolate False inp) (interpolate True inp)
