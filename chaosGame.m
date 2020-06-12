% script for playing the chaos game

% Chaos game explanation: 
% The chaos game starts with a regular polygon. When you start, you choose
% a random vertice to start from. Each iteration of the game, you randomly 
% choose another point and travel a distance of abs(xnow - xnext) *
% distance_factor. You do this over and over again until the iterations are
% moved. 
%
% What is interesting is that the effect of te scaling factor. Notably,
% each polygon has a scaling factor "limit" where it descends from nice
% fractal patterns into randomized chaos. It then reaches a second "limit"
% where the point distribution transitions from a random noise into a line.
%
% I wonder if there's a probabilistic proof which explains the first factor
% where it goes from fractals to chaos. To see why it ends up in fractals,
% it's clear that if the factor is decently big then the points tend to
% cluster in the same areas. This is because the points sort of bounce
% around when the factor gets large, intuitively because pairing up the 
% other points which aren't your current one indicates that each
% equidistant point probability is equally likely. As such, you get a
% pretty even distribution of points in the shape of smaller polygons
% as the chosen points bounce around to different clusters.
%
% As mentioned above, I'm not sure if there's a factor when they suddenly
% stop making a fractal-like shape. Intuitively, this happens when distances 
% get too close to each other to cluster and the points end up all over the
% place. I'd love to see a proof explaining this some day
%
% The line interested me the most because it reminded me of a gradient descent
% type of problem except that it is controlled probabilistically. IF you
% choose a tiny factor like 1/10000, you see the points start to form a
% line to the center. This is because intuitively, the distance from the
% far ends is bigger than the distance from the close ends, meaning that
% the contribution from those points makes a bigger impact to inch the
% points closer to the center. Furthermore, the up and down points kind of
% balance out because they are roughly equally distributed. So, the net
% result is the up and down cancel and the points move closer and closer to
% the middle.
% 

numIterations = 10000;
clf;
figure(1)

factor = 19/32;
shift = 1;
range = 0;

discrete = 1;
degrees = 0:discrete:360-discrete;
r = 1;
% circle and see what happens
x = r * cos(degrees * pi / 180);
y = r * sin(degrees * pi / 180);
vertices = [x', y'];
realRs = sqrt(x.^2 + y.^2);
% vertices = [0, 0;
%             4, 0;
%             0, 4;
%             4, 4];
% vertices = [0, 0;
%             6, 0;
%             3, 3*sqrt(3)];
% move up by like 5
vertices = [6 * cos(0.314) + 6, 6 * sin(0.314) + 6;
            6, 12;
            6 * cos(-0.942478) + 6, 6 * sin(-0.942478) + 6;
            -6 * cos(0.314) + 6, 6 * sin(0.314) + 6;
            -6 * cos(-0.942478) + 6, 6 * sin(-0.942478) + 6]; 
totalArray = zeros(numIterations + size(vertices, 1), 2);
for i = 1:size(vertices, 1)
    totalArray(i, :) = vertices(i, :);
end
numVerts = size(vertices, 1);
startPoint = vertices(randi(numVerts), :);
scatter(totalArray(:, 1), totalArray(:, 2));

for j = 1:numIterations
    newPoint = chaosGameGenerator(startPoint, vertices, factor);
    % newPoint = chaosGameGeneratorNoise(startPoint, vertices, factor, shift, range);
    totalArray(j + numVerts, :) = newPoint;
    startPoint = newPoint;
    % scatter(totalArray(:, 1), totalArray(:, 2));
    % pause(1);
end
scatter(totalArray(:, 1), totalArray(:, 2));

    
        
