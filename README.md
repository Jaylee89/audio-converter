# Audio Converter

The tool depends on FFmpeg to convert audio format

## Setup

1. Add executable permisssion for `start.sh`, `install.sh`
   - `chmod a+x start.sh`
   - `chmod a+x install.sh`
1. Run `install.sh`
1. Activite Virtual Env
   1. Mac: `source venv/bin/activate`
   1. Or Win32: `source venv/Scripts/activate`

## To get audio property

```bash
python3 demo.py
```

## Convert audio to .mp3

```bash
ffmpeg -i input/filename.arm output/filename-output.mp3
```

## How to install `ffmpeg` library on Mac, refer to [here](https://www.jianshu.com/p/73441acf7815)

```bash
# Or, follow it to install
# install brew
./brew-intall.rb
# verify brew installation
brew --help
# install ffmpeg
brew install ffmpeg
# verify ffmpeg installation
ffmpeg --help
```

## Failed to connect to raw.githubusercontent.com port 443: Connection refused error:

Add the IP to hosts file, refer to [here](https://blog.csdn.net/ccgshigao/article/details/108169891)

If operation failed to the hosts file, please follow below:

1. open /etc/hosts via external text software
1. add 151.101.76.133 raw.githubusercontent.com last line

## [ffmpeg doc](http://ffmpeg.org/ffmpeg.html)

or https://www.cnblogs.com/chen1987lei/archive/2010/12/03/1895242.html

## [learning courses from CSDN audio](https://edu.csdn.net/course/detail/2314)