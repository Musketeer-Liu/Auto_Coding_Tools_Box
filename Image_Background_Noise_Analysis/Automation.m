% ---- Script Illustration Module ----
disp('---- -------------------------- ----');
disp('---- Script Illustration Module ----');
disp('---- -------------------------- ----');
% Explain how to operate this script
disp('Author: Yutong Liu | Release Date: Apr. 13, 2018 | Email: musketeer.liu@gmail.com');
disp('Copy and Paste Automation.m to the folder having the data you want to analysis and open MATLAB software');
disp('Click Automation.m for description and/or Drag this Automation.m into Matlab Console for automated analysis');
disp('When opening the excel, please ignore the unsafe/croptted message from excel, just select Yes after processing');
disp('When closing the excel, please select do not save the data option, it is already saved');
disp('If you have multiple test to run, remeber to delete the variables in Workspace and close the excel first');
disp('If you want to redo the analysis on the same dataset, please copy the folder and redo it in the new folder');




% ---- Pre Display Module ----
disp('---- ------------------ ----');
disp('---- Pre Display Module ----');
disp('---- ------------------ ----');
% Setup the file system with relative method start with current and the Result Excel folder:
file_path = './';
results_path = '../';
absolute_path = pwd;
disp(['Original File path is current folder: ', absolute_path]);
disp("Original File path is parent folder: '../', you may also set new result path instead");
disp("If you do not want to change Result Combination File Path, just type in '../'");
results_path = input('Please set the path of results.xls (Please with Quotation): ');


% Setup file counting system:
%count_1 = 0;
%count_2 = 0;


% Display and count all the files (not folders) in current folder before operation:
disp('File List before this Operation: ');
contains_before = dir(file_path);
count_1 = length(contains_before);

for k = 1: length(contains_before)

if (contains_before(k).isdir)
continue;
%count_1 = count_1 + 1;
end

disp(contains_before(k).name);
end


% Create the excel for the analysis data:
head = fopen('analysis.xls', 'w+');
fprintf(head, 'Time \t');
fprintf(head, 'Sample \t');
fprintf(head, 'Average \t');
fprintf(head, 'STDEV \n');




% ---- Real Automation Module ----
disp('---- ---------------------- ----');
disp('---- Real Automation Module ----');
disp('---- ---------------------- ----');
% Find all the files in the folder with .lsb_raw extension (*.lsb_raw):
file_list = dir([file_path, '*.lsb_raw']);
count = length(file_list);
avg_sum = 0;
std_sum = 0;

if count > 0

for i = 1: count
full_name = file_list(i).name;


% Calculate the Average and STDEV
test = fopen(full_name);
data = fread(test);
trim = data(1:2:end);
avg = mean2(trim);
std = std2(trim);
matrix = vec2mat(trim, 400);
avg_sum = avg_sum + avg;
std_sum = std_sum + std;

% Process the full_name to remove path and extension amd Acquire pure image_name
[path, image_name, ext] = fileparts(full_name);
current = datestr(now, 31);


% Write the analysis into the analysis Excel:
analysis = fopen('analysis.xls', 'a+');
fprintf(analysis, [current, '\t']);
fprintf(analysis, [image_name, '\t']);
fprintf(analysis, '%10.8f \t ', avg);
fprintf(analysis, '%10.9f \t', std);
fprintf(analysis, '\r\n');
fclose(analysis);


% Plot Histogram and save the image in both .bmp and .fig format:
hist = histogram(matrix);
hist_bmp = ['hist_', image_name, '.bmp'];
saveas(hist, hist_bmp);
hist_fig = ['hist_', image_name, '.fig'];
saveas(hist, hist_fig);


% Plot Histogram and save the image in both .bmp and .fig format:
heat = heatmap(matrix);
heat_bmp = ['heat_', image_name, '.bmp'];
saveas(heat, heat_bmp);
heat_fig = ['heat_', image_name, '.fig'];
saveas(heat, heat_fig);


end

end


% Calculate the Average of the Average and STDEV:
avg_mean = avg_sum/count;
std_mean = std_sum/count;
finish = datestr(now, 31);

% Write the result into results Excel:
results = fopen([results_path, 'results.xls'], 'a+');
fprintf(results, [finish, '\t']);
fprintf(results, [image_name, '\t']);
fprintf(results, '%10.8f \t', avg_mean);
fprintf(results, '%10.9f \t', std_mean);
fprintf(results, '\r\n');
fclose(results);



% ---- Post Display Module ----
disp('---- ------------------- ----');
disp('---- Post Display Module ----');
disp('---- ------------------- ----');
% Display all the files (not folders) in current folder after operation:
disp('File List after this Operation: ');

contains_after = dir(file_path);
count_2 = length(contains_after);

for k = 1: length(contains_after)

if (contains_after(k).isdir)
continue;
%count_2 = count_2 + 1;
end

disp(contains_after(k).name);
end 


% Display how many files were created:
add_count = count_2 - count_1;
disp([add_count, ' new files were created during this running']);