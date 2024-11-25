require 'csv'

CSV.open("fixed.csv", "wb") do |csv|
  CSV.foreach('image_search_output_b.csv', liberal_parsing: true, row_sep: "\r\n") do |row|
    csv << [row[0], row[1], row[2]&.rstrip]
  end
end
