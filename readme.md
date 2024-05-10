# Zahli

## What is it?
Zahli is a simple German voice / speech bot that performs calculations.

## Main Features
The application provides the following functionality:
- German speech recognition interface
- Parsing of mathematical expressions from formulated questions
- Calculation and output of the result

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/c4ristian/zahli

## Setup
```sh
conda env create -f environment.yml

conda activate zahli
```

## Run Tests
```sh
pytest
```

## Code Coverage
```sh
pytest --cov
```

## Code Quality
```sh
pylint FILENAME.py
```

## Run application
```sh
python main.py
```

Silent mode:
```sh
python main.py -s
```

## Trouble Shooting

Under Windows, if a problems with *portaudio* occurs, reinstall the package manually:

```sh
conda install portaudio
```

Under Windows, if the following error occurs: *OSError:FLAC conversion utility not available*, perform these steps:
- Navigate to the anaconda env directory "...user\anaconda3\envs\zahli\Library\bin" 
- rename the file "flac.exe" to "flac"

## License
[Apache 2.0](LICENSE.txt)


## Contact us
[christian.koch@th-nuernberg.de](mailto:christian.koch@th-nuernberg.de)
