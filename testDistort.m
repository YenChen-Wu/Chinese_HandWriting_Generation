len = 100;
backImg = zeros(len,len);
location = 'data2/';
outlocation = 'output/erosion1_data2/';
angle = 3;
cut = 15;
ero = 1;

for i=1:420
	filename = sprintf('%d.jpg',i);
    locatename = strcat(location, filename);
    img = imread(locatename);
    img = rgb2gray(img);
    % rotate 
    %{
    img = imrotate(img,angle);
    img = img(cut:size(img,1)-cut, cut:size(img,1)-cut);
    %}

    % erosion
    %
    se = strel('ball',ero,ero);
    img = imerode(img, se);
    %

    % Gaussian noise
    %img = imnoise(img,'gaussian',0,0.01);

    rimg = imresize(img, [len len]);
    outname = strcat(outlocation, filename);
    imwrite(rimg, outname);
    %imshow(rimg);
end