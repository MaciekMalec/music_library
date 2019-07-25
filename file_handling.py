def import_data(filename='text_albums_data.txt'):
    albums = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for row in lines:
            rows = row.strip().split(',')
            albums.append(rows)
        return albums

def export_data(albums, filename='text_albums_data.txt', mode='a'):
    if mode not in ["w", "a"]:
        raise ValueError('Wrong write mode')
    with open(filename, mode) as f:
        for line in albums:
            row = ",".join(line)
            f.write(row + "\n") 