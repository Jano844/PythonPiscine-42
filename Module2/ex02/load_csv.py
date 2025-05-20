
import sys
import os
import pandas as pd

def load(path: str) -> pd.DataFrame:
    """
    Check it the Path exists

    Return an pandas.DataFrame of the CSV
    """

    path = path.strip()
    if not os.path.exists(path):
        return None
    if not path.lower().endswith('.csv'):
        return None


    df = pd.read_csv(path)
    return df


def main():
    argc = len(sys.argv)
    argv = sys.argv

    if argc == 2:
        Dataframe = load(argv[1])
        if Dataframe is not None:
            # .head to print only first few Lines, if the Data gets to big
            print(Dataframe.head)
    else:
        print("Error, Wrong Input")
    return



if __name__ == "__main__":
    main()
