len = 100;
backImg = zeros(len,len);
location = 'data1/';
outlocation = 'output/data1/';

for i=1:510
	filename = sprintf('%d.jpg',i);
    locatename = strcat(location, filename);
    img = imread(locatename);
    img = rgb2gray(img);
    rimg = imresize(img, [len len]);
    outname = strcat(outlocation, filename);
    imwrite(rimg, outname);
end