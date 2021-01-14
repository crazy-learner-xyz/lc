思路(Python)\

Maybe get a dictionary such that there's a mapping between each index of the original S and the corresponding characters. And if there's a new source/target to be replaced, then get all the index related to that, and replace it with the target, and if there are len(s) > len(t), then put all the extra letters in the last index, if len(s) < len(t), then clean the last indices and that's it. 

Why don't I just keep a copy of the original S. 

Speed is a bit low, might want to find ideas that are faster than this.