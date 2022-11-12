
# Data Engineer test - Tinybird - MySolution

This is a solution for the technical test for the 
data engineer position

## Usage

This program return all the trips over 0.9 percentile 
in distance traveled of a PARQUET file from 
NYC “Yellow Taxi” Trips Data

It shows you the record on console and dumps the data into a 
csv file to easy handling

### How it works

When you execute the program it shows a window to select the 
PARQUET file you want the data

[![Captura-de-pantalla.png](https://i.postimg.cc/13CPrbKc/Captura-de-pantalla-2022-11-12-a-las-12-13-29.png)](https://postimg.cc/RWHjMsyN)

When you select the file, it is going to shows, in console the 
records over 0.9 in distance traveled and it is going to download
a csv file into the path where you have the script hosted

[![Captura-de-pantalla-2022-11-12-a-las-12-15-38.png](https://i.postimg.cc/5NzFGqrC/Captura-de-pantalla-2022-11-12-a-las-12-15-38.png)](https://postimg.cc/ZCTRv34b)

### Manipulate the csv

To see the data inside the csv file you can use Excel

[![Captura-de-pantalla-2022-11-12-a-las-12-17-39.png](https://i.postimg.cc/PxtGDjLM/Captura-de-pantalla-2022-11-12-a-las-12-17-39.png)](https://postimg.cc/yJrrq2yJ)

## Run Locally

Clone the project

```bash
  git clone https://github.com/rbngrc/Data-Engineer-test---Tinybird---MySolution.git
```

Go to the project directory

```bash
  cd Data-Engineer-test---Tinybird---MySolution
```

Install dependencies (if you don't have it already)

```bash
  pip install tkinter pandas
```

Start the project

```bash
  python parquet_script.py
```


## Documentation

[Reading Parquet Files in Python](https://www.youtube.com/watch?v=XFO5jdGsMek&ab_channel=DataEngUncomplicated)

[Python GUI open a file (filedialog)](https://www.youtube.com/watch?v=q8WDvrjPt0M&ab_channel=BroCode)

[Pandas query Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.query.html)

[Pandas to_csv Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)

[NYC Trips Data](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
## Authors

- Rubén García - [@rbngrcdz](https://www.github.com/rbngrc)

