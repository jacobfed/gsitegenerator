"""Docstring."""
# Build Static HTML site form directory of HTML templates and plain files.
import json
import os
import shutil
import jinja2
import click


# Creating command-line arguments
@click.command(help='Templated static website generator.')
@click.option('--verbose', '-v', is_flag=True,
              help='Print more output.', default=False)
@click.argument('input_dir', nargs=1)
# main function
def main(verbose, input_dir):
    """Docstring."""
    try:
        # Setup new html directory
        html_path = os.path.abspath(input_dir + '/html')

        # Read in JSON file
        datastore = json.load(open(os.path.abspath(input_dir
                                                   + '/config.json')))
        path_to_outputfile = html_path
        # for loop to iterate through list pages
        template_dir = os.path.abspath(input_dir + '/templates/')

        template_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir),
            autoescape=jinja2.select_autoescape(['html', 'xml']),)
        # Check for css file and add to html directory if necessary
        if os.path.exists(os.path.abspath(input_dir + '/static/')):
            shutil.copytree(os.path.abspath(input_dir + '/static/'),
                            os.path.abspath(input_dir + '/html/'))
            if verbose:
                print('Copied ' + input_dir + '/static/ -> '
                      + input_dir + "/html/")
        # Creating html directory if copying over files not done
        else:
            os.mkdir(html_path)

        # Iterate through each item in the config.json list, render it,
        # and write to output file
        for index in datastore:
            template = template_env.get_template(index['template'])
            output = template.render(index['context'])

            # Setup mkdir setup TODO
            if not os.path.exists(os.path.abspath(input_dir + '/html' +
                                                  index['url'])):
                os.makedirs(os.path.abspath(input_dir +
                                            '/html' + index['url']))
            path_to_outputfile = os.path.abspath('../../Public' + '/html' +
                                                 index['url'] + index['template'])
            print(os.path.abspath(input_dir + '/html' + index['url'] + index['template']))
            outputfile = open(path_to_outputfile, 'w')
            outputfile.write(output)
            # Verbose output
            if verbose:
                print('Rendered ' + index['template']
                      + ' -> ' + input_dir +
                      '/html' + index['url'] + index['template'])
    except jinja2.TemplateError:
        print('Error_Jinja')
        exit(1)
    except ValueError:
        print('Error_JSON')
        exit(1)
    except FileNotFoundError:
        print('Error_FileNotFound')
        exit(1)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
