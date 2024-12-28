# main.py
from awards_data import award_list_options

def count_awards(movie_title):
    count = 0
    movie_title = " ".join(movie_title.lower().split())
    for award_option in award_list_options:
        for movie in award_option:
            movie = " ".join(movie.lower().split())
            if movie == movie_title:
                count += 1
    return count

def print_award_winners(awards):
    awards = awards.lower()
    for award_option in award_list_options:
        if awards == award_option.lower():
            award_winners = "\n".join(award_option)
            return award_winners
    return None

def main():
    user_num = int(input(('\nSelect 1 to search a specific movie, 2 to print specific awards results, 0 to end: ')))

    while user_num != 0:
        if user_num == 1:
            movie_title = input('Please enter the movie title you would like to search: ')
            print('--Number of Awards Won--\n{}'.format(count_awards(movie_title)))
            user_num = int(input(('\nSelect 1 to search a specific movie, 2 to print specific awards results, 0 to end: ')))

        elif user_num == 2:
            awards = input('\nPlease choose one of the following awards lists:\nOscars\nSAG\nNBR\nISA\nGLAAD\nNAACP\n\n')
            award_winners = print_award_winners(awards)
            if award_winners != None:
                print('--Requested Award Winners--\n{}'.format(award_winners))
            else:
                print('Awards list not found.')
            user_num = int(input(('\nSelect 1 to search a specific movie, 2 to print specific awards results, 0 to end: ')))
        else:
            print('You must select either 1, 2, or 0.')
            user_num = int(input(('\nSelect 1 to search a specific movie, 2 to print specific awards results, 0 to end: ')))

    if user_num == 0:
        print('Thank you for using the awards data program.')

if __name__ == "__main__":
    main()
