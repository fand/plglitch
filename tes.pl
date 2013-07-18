my $s = "asddgjnbk01wbdaf;lji;lifjkerrghd00dcfkghsdfksdfklkjdghlkjdh";

my @a = split /(00dc|01wb)/, $s;
for (@a) {
    print $_ . "\n";
}
print scalar @a . "\n";


print "-------------------------------------\n";

my ($p, $q) = (1*10, 1*100);
print "p: $p\nq: $q\n";
