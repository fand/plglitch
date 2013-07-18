open IN, '<', $ARGV[0];
read IN, my $buf, -s $ARGV[0];
my ($movi, $idx1) = (index($buf, "movi"), index($buf, "idx1"));
my @frames = map {[unpack('a4VVV', substr($buf, $idx1+8+$_*16, 16))]} 0..((unpack('V', substr($buf, $idx1+4, 4)) / 16)-1);
my ($movi_new, $idx1_new, $first) = ("movi", substr($buf, $idx1, 8), 1);
for (@frames) {
    if (@$_[0] =~ /00d./ && @$_[1] & 0x10 && $first == 0) {
        $movi_new .= @$_[0] . "\x00\x00\x00\x00";
    }
    else {
        $first = 0 if $first;
        $movi_new .= substr($buf, $movi + @$_[2], @$_[3] + 8);
        $movi_new .= "\x00" if length($movi_new) % 2 == 1;
        $idx1_new .= pack('a4VVV', @$_);
    }
}
open OUT, '>', $ARGV[1];
print OUT substr($buf, 0, $movi) . $movi_new . $idx1_new;
