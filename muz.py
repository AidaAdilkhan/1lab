import random
import argparse
from glob import glob
from os import path
from pprint import pprint


class Crawler:
    def __init__(self, input_directory):
        self.input_directory = input_directory

    def get_all_songs_list(self):
        all_songs_list = []
        for file in glob(f'{self.input_directory}/s*.txt'):
        for file in glob('s*.txt'):
            with open(file, encoding='UTF-8') as input_file:
                all_songs_list.extend(input_file.readlines())
            print(all_songs_list)
            while '\n' in all_songs_list:
                all_songs_list.remove('\n')
        return all_songs_list


class Generator:
    def __init__(self, all_songs_list):
        self.all_songs_list = all_songs_list
        print(self.all_songs_list)

    def generate_song_chunk(self, n_rows):
        return random.sample(self.all_songs_list, n_rows)

    def generate_song(self, chorus_n_rows=3, couplet_n_rows=3):
        new_songs_list = []
        chorus = self.generate_song_chunk(chorus_n_rows)
        for i in range(3):
            couplet = self.generate_song_chunk(couplet_n_rows)
            for el in couplet:
                new_songs_list.append(el)
            new_songs_list.append('\n')
            for el in chorus:
                new_songs_list.append(el)
            new_songs_list.append('\n')
        pprint(new_songs_list)
        return new_songs_list


class Saver:
    def __init__(self, output_directory, generated_list):
        self.output_directory = output_directory
        self.generated_list = generated_list

    def save_new_song(self):
        # with open(path.join(self.output_directory, 'new_song.txt'), 'w+', encoding='UTF-8') as output_file:
        with open('new_song.txt', 'w+', encoding='UTF-8') as output_file:
            output_file.writelines(self.generated_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-ch',  '--chorus', required=True)
    parser.add_argument('-cp', '--couplet', required=True)
    args = vars(parser.parse_args())

    couplet_n_rows = int(args['couplet'])
    chorus_n_rows = int(args['chorus'])

    crawler = Crawler('input')
    generator = Generator(all_songs_list=crawler.get_all_songs_list())
    saver = Saver(output_directory='output',
                  generated_list=generator.generate_song(chorus_n_rows=chorus_n_rows,
                                                         couplet_n_rows=couplet_n_rows)
                  )
    saver.save_new_song()
