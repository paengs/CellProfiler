import os
import sys
import logging
import logging.config

PATH = None

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
    img = io.imread('samples/test.jpg')
    img = io.imread(PATH)
    img_dict = {'input':img }
    count = pipeline.count_cell(img_dict)
    print count
    """ gen cell map example
    count = pipeline.gen_cell_map(img_dict)
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.imshow(img)
    plt.imshow(count, cmap=cm.jet, alpha=0.8, vmin=0.0, vmax=1.0)
    plt.axis('off')
    plt.show()
    """
if __name__ == "__main__":
    import sys
    sys.path.append('../')
    PATH=sys.argv[1]
    #main('samples/cell_detection.cppipe')
    main('samples/tupac.cppipe')
