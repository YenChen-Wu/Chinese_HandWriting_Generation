large_len = 150;
len = 100;
backImg = zeros(large_len,large_len);
location = 'fonts/type10_3000/';
outlocation = 'output/';

for i=1:50
    filename = sprintf('%d.png',i);
    locatename = strcat(location, filename);
    [img, map, alpha] = imread(locatename);
    if (sum(max(img))>100)
        [height width] = size(img);
        backImg(large_len-height+1:large_len,1:width) = img;
        backImg = backImg .* (-1) +1;
        rimg = imresize(backImg, [len len]);
        olocatename = strcat(outlocation,filename);
        imwrite(backImg, olocatename);
        backImg = zeros(large_len,large_len);
    end
end

