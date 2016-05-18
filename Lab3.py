import pandas
import numpy
import timeit


def opn():
    df = pandas.read_csv("/home/KPI2course/SRP/Lab2/data.txt", low_memory=False, sep=";", na_values='?')
    return df.dropna(how='any')


def get_gap(df):
    df = df[df['Global_active_power'] > 5]
    print(df['Global_active_power'])


def get_v(df):
    df = df[df['Voltage'] > 235]
    print(df['Voltage'])


def get_gi(df):
    df = df[(df['Global_intensity'] >= 19) & (df['Global_intensity'] <= 20) & (df['Sub_metering_2'] > df['Sub_metering_3'])]
    print(df['Global_intensity'])


def get_av(df):
    df = df.sample(n=500000)
    print("Average SB_1: ", df['Sub_metering_1'].sum() / len(df['Sub_metering_1']),
          ", average SB_2: ", df['Sub_metering_2'].sum() / len(df['Sub_metering_2']),
          ", average SB_3: ", df['Sub_metering_3'].sum() / len(df['Sub_metering_3']))


def get_5(df):
    df = df[(df['Time'] > "18:00:00") & (df['Global_active_power'] > 6) & (df['Sub_metering_2'] > df['Sub_metering_3']) &
            (df['Sub_metering_2'] > df['Sub_metering_1'])]
    df = [df[:int(len(df.index)/2):3], df[int(len(df.index)/2)::4]]
    print("First half: ", df[0][['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']],
          "Second half: ", df[1][['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']])


def n_opn():
    arr = numpy.genfromtxt("/home/KPI2course/SRP/Lab2/data.txt", delimiter=";", missing_values='?',
                           filling_values=-1, names=True, dtype="U8, U8, <f8, <f8, <f8, <f8, <f8, <f8, <f8")
    return arr[numpy.nonzero(arr['Global_active_power'] >= 0)]


def n_get_gap(arr):
    arr = arr[numpy.nonzero(arr['Global_active_power'] > 5)]
    print(arr['Global_active_power'])


def n_get_v(arr):
    arr = arr[numpy.nonzero(arr['Voltage'] > 235)]
    print(arr['Voltage'])


def n_get_gi(arr):
    arr = arr[numpy.nonzero((arr['Global_intensity'] >= 19) & (arr['Global_intensity'] <= 20) &
                            (arr['Sub_metering_2'] > arr['Sub_metering_3']))]
    print(arr['Global_intensity'])


def n_get_av(arr):
    arr = numpy.random.choice(arr, size=500000)
    print("Average SB_1: ", numpy.sum(arr['Sub_metering_1']) / len(arr['Sub_metering_1']),
          ", average SB_2: ", numpy.sum(arr['Sub_metering_2']) / len(arr['Sub_metering_2']),
          ", average SB_3: ", numpy.sum(arr['Sub_metering_3']) / len(arr['Sub_metering_3']))


def n_get_5(arr):
    arr = arr[numpy.nonzero((arr['Time'] > '18:00:00') & (arr['Global_active_power'] > 6) &
                            (arr['Sub_metering_2'] > arr['Sub_metering_3']) &
                            (arr['Sub_metering_2'] > arr['Sub_metering_1']))]
    arr = numpy.array_split(arr, indices_or_sections=2)
    arr[0] = arr[0][numpy.arange(0, arr[0].shape[0], 3)]
    arr[1] = arr[1][numpy.arange(0, arr[1].shape[0], 4)]
    print("First half: ", arr[0][['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']],
          "Second half: ", arr[1][['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3']])

#df = opn()
#arr = n_opn()

start = timeit.default_timer()
#get_v(df)
print(timeit.default_timer() - start)
