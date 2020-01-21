#To use conditional statement if-else

#!/usr/bin/perl
print"Type Yes or No\n";
$word=<STDIN>;

$upper=lc $word ;
if ($upper eq "yes")
{
 print "\nYour answer is Yes\n"
}

else
{print "\nYour answer is No\n"
};
exit




