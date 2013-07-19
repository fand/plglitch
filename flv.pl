open $f_in, '<', $ARGV[0];
read $f_in, my $buf, -s $ARGV[0];
my ($buf_new, $i, $first) = ("", 13, 1);
while ($i < length $buf) {
    my $l = (substr($buf, $i, 1) =~ /\x08|\x09|\x12/) * (unpack('N', substr($buf, $i+1, 4)) >> 8);
    if (substr($buf, $i, 20) =~ /^\x09.{10}(.).*$/ && unpack('B8', $1) =~ /^0001....$/ && rand(10) < 7) {
        $first? ($first = 0) : (substr($buf, $i, $l+15, "") && ($i -= ($l + 15)));
    }
    $i += 11 + $l + 4;  # tag + size + lasttagsize
}
open $f_out, '>', $ARGV[1];
print $f_out $buf;
