import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': "C:\\Users\\Admin\\OneDrive\\Desktop\\all-project-files\\chicago.csv",
              'new york': "C:\\Users\\Admin\\OneDrive\\Desktop\\all-project-files\\new_york_city.csv",
              'washington': "C:\\Users\\Admin\\OneDrive\\Desktop\\all-project-files\\washington.csv" }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city =(input("Would you like to see data for Chicago, New York, or Washington? ")).lower()
            break
        except:
            print("try again ,invalid inputs")

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month =(input(" Which month - January, February, March, April, May, or June? ")).lower()
            break
        except:
            print("try again ,invalid inputs")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day =(input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ")).title()
            break
        except:
            print("try again ,invalid inputs")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june','july',' August','September','October','November',' December']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month=df['month'].mode()[0]
    print("the most common month: {}".format(most_month))
    df.head()
    # display the most common day of week
    most_day=df['day_of_week'].mode()[0]
    print("the most common day of week: {}".format(most_day))
    # display the most common start hour
    df['start hour']=df['Start Time'].dt.hour
    most_hour=df['start hour'].mode()[0]
    print("the most common start hour: {}".format(most_hour))

    display_raw(df)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_Start_Station=df['Start Station'].mode()[0]
    print("the most commonly used start station: {}".format(most_Start_Station))
    # display most commonly used end station
    most_End_Station=df['End Station'].mode()[0]
    print("the most commonly used end station: {}".format(most_End_Station))

    # display most frequent combination of start station and end station trip
    df['combination station']=df['Start Station']+df['End Station']
    most_Station=df['combination station'].mode()[0]
    print("the most frequent combination of start station and end station trip: {}".format(most_Station))

    display_raw(df)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total travel time : {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('mean travel time : {}'.format(df['Trip Duration'].mean()))

    display_raw(df)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count=df['User Type'].value_counts()
    print("counts of user types : {}".format(user_count))
    # Display counts of gender
    try:
      gender_count = df['Gender'].value_counts()
      print("counts of user types : {}".format(gender_count))
    except:
        print("there is no gender in the dataframe you choose ")

    # Display earliest, most recent, and most common year of birth
    try:
      earliest=df['Birth Year'].min()
      recent=df['Birth Year'].max()
      most_birth=df['Birth Year'].mode()[0]
      print("earliest year of birth : {}".format(earliest))
      print("most recent year of birth : {}".format(recent))
      print("most common year of birth : {}".format(most_birth))
    except:
        print("there is no birth year in the dataframe you choose ")

    display_raw(df)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw(df):
    row_index = 0
    while True:
        user_input = input("Would you like to see 5 lines of raw data? Type 'yes' or 'no': ").lower()

        if user_input == 'yes':
            # Display the next 5 lines of data
            end_index = row_index + 5
            if row_index < len(df):
                print(df.iloc[row_index:end_index])
                row_index = end_index
            else:
                print("No more data to display.")
                break
        elif user_input == 'no':
            print("Ending raw data display.")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
