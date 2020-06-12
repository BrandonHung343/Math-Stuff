function [outputPoint] = chaosGameGeneratorNoise(point, vertices, factor, range, scale)
%UNTITLED2 Summary of this function goes here
%   vertices = n x 2
%   point = 1 x 2
    x = point(1);
    y = point(2);
    numVerts = size(vertices, 1);
    rolledIndex = randi(numVerts);
    rolledPoint = vertices(rolledIndex, :);
    rolledX = rolledPoint(1);
    rolledY = rolledPoint(2);
    dx = rolledX - x;
    dy = rolledY - y;
    noise = (rand(1) * scale) + range;
    outputPoint = [x + factor*dx*noise, y + factor*dy*noise] ; 
end

