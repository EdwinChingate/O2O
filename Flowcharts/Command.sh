gimp -i -b '(let* ((image (car (gimp-file-load RUN-NONINTERACTIVE "DarkFlowcharts/JoinSpectra.svg" "DarkFlowcharts/JoinSpectra.svg" )))(drawable (car (gimp-image-active-drawable image))))(gimp-invert drawable)(file-png-save RUN-NONINTERACTIVE image drawable  "DarkFlowcharts/JoinSpectra.svg" "DarkFlowcharts/JoinSpectr.svg" 0 0 0 0 0 1 1)(gimp-quit 0))'
