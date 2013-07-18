my $CODE = "00db";  # frame start code
open IN, '<', $ARGV[0];
read IN, my $buf, -s $ARGV[0];
open OUT, '>', $ARGV[1];
print OUT join $CODE, grep { !($_ =~ "^.{6}\x01\xB0") } split($CODE, $buf);
