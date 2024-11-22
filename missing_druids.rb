require 'csv'

### Find any druids that we forgot to get into out.csv
expected_druids = []

# Open and read the CSV file
CSV.foreach('report.csv', headers: true) do |row|
  expected_druids << row[0]
end

completed_druids = []

# Open and read the CSV file
CSV.foreach('out.csv', headers: true) do |row|
  completed_druids << row[0]
end

puts expected_druids - completed_druids
