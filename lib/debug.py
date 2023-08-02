import ipdb

from classes.magazine import Magazine
from classes.reader import Reader
from classes.subscription import Subscription


vogue = Magazine("vogue")
time = Magazine("time")

xtina = Reader("xtina", "xtina@mail.com")
sean = Reader("sean", "sean@mail.com")

sub1 = Subscription(vogue, xtina, 30.00)
sub2 = Subscription(time, xtina, 24.99)
sub3 = Subscription(time, sean, 12.99)

ipdb.set_trace()
