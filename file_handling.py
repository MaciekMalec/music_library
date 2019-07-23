def import_data(filename='text_albums_data.txt'):
    albums = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for row in lines:
            rows = row.strip().split(',')
            albums.append(rows)
        return albums

# print(import_data())