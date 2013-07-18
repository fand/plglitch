use strict;
use Carp;
use FFmpeg::Command;

my $ffmpeg = FFmpeg::Command->new('/Users/youpy/Desktop/ffmpeg');
my $output_file = 'out.avi';

$ffmpeg->input_options({
    file => shift,
                       });

$ffmpeg->timeout(300);
$ffmpeg->output_options({
    file                => $output_file,
    video_codec         => 'libxvid',
    format              => 'avi',
    });

# disable audio
#push @{ $ffmpeg->options }, '-an';

push @{ $ffmpeg->options }, qw/-sameq -aspect 4:3/;
#push @{ $ffmpeg->options }, qw/-sameq/;

my $result = $ffmpeg->exec();
croak $ffmpeg->errstr unless $result;
