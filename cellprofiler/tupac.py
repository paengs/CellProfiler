import os
import sys
import logging
import logging.config

def main(pipeline_path):
    ''' Run CellProfiler '''
    import cellprofiler.preferences as cpprefs
    cpprefs.set_awt_headless(True)
    cpprefs.set_headless()
    set_log_level()
    try:
        run_pipeline_headless(pipeline_path)
    except Exception, e:
        logging.root.fatal("Uncaught exception in CellProfiler.py", exc_info=True)
        raise

def set_log_level():
    '''Set the logging package's log level based on command-line options'''
    log_level = 50 # Only FATAL errors will be displayed.
    try:
        logging.root.setLevel(int(log_level))
        if len(logging.root.handlers) == 0:
            logging.root.addHandler(logging.StreamHandler())
    except ValueError:
        logging.config.fileConfig(log_level)

def run_pipeline_headless(pipeline_path):
    '''Run a CellProfiler pipeline in headless mode'''
    from cellprofiler.pipeline import Pipeline
    pipeline = Pipeline()
    pipeline.load(pipeline_path)

    from skimage import io
    img = io.imread('/home/paeng/projects/5__LUNIT/1__PATHO/tupac16/data/TUPAC-TE-001/roi_results/0/crop_0_0.jpg')
    img_dict = {'input':img }
    count = pipeline.count_cell(img_dict)
    print count

if __name__ == "__main__":
    import sys
    sys.path.append('../')
    main('/home/paeng/projects/5__LUNIT/1__PATHO/tupac16/docker/cell_detection_pipeline.cppipe')
