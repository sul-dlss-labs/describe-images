require 'csv'

CSV.open("fixed.csv", "wb") do |csv|
  CSV.foreach('image_search_output_b.csv') do |row|
    csv << [row[0], row[1], row[2]&.rstrip]
  end
end
