from plotnine import ggplot, geom_point, geom_smooth, aes, geom_vline, geom_text, geom_label
from pandas import to_datetime

def plot_and_save(scale_data_df_cleaned, smooth_factor, temp_file_name):
    fasting_start = to_datetime('2019-10-15')
    plot_output = (ggplot(scale_data_df_cleaned, aes(x = 'timestamp', y = 'weight')) + 
        #   facet_wrap('~', ncol = 1, scales = 'free') +
        geom_point(size = 0.5) +
        geom_smooth(span = smooth_factor, color = 'red') +
        geom_vline(aes(xintercept = fasting_start), color = 'blue', size = 1.2) +
        geom_label(aes(x = to_datetime('2019-11-30'), y = max(scale_data_df_cleaned.loc[:,'weight'])), label = 'IF starts!', size = 15)
    )
    plot_output.save(temp_file_name, width = 13, height = 10, dpi = 80)