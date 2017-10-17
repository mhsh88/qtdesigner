clear;
files = dir('*.svg');
% name = cell();
m = 1;
for file = files'
    
name(m,:) = {['<file>icon/', file.name, '</file>']};

m = m +1;
end