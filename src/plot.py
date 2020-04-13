from plotnine import ggplot, geom_point, geom_smooth, aes

def plot_and_save(scale_data_df_cleaned, temp_file_name):
    plot_output = (ggplot(scale_data_df_cleaned, aes(x = 'timestamp', y = 'weight')) + 
        #   facet_wrap('~', ncol = 1, scales = 'free') +
        geom_point(size = 0.5) +
        geom_smooth(span = 0.1, color = 'red')
    )
    plot_output.save(temp_file_name, width = 12, height = 8, dpi = 100)