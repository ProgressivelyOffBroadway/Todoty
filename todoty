#!/usr/bin/env ruby 

require './styling'
require 'optparse'

file = ""
opts_ = ""
options = {}
### Handle flags ###
OptionParser.new do |opts|
  # Banner for the CLI help documentation
  opts.banner = "Usage: todoty [options] [file/directory]"

  # Save the help documentation in a non local variable no matter what
  opts_ = opts

  # Help flag
  opts.on("-h", "--help", "Print available commands") do
    puts opts
  end

  # Directory flag
  opts.on("-d", "--directory [DIR]", "Run todoty on directory" ) do |d|
    options[:directory] = d
  end

  # Explicit file flag
  opts.on("-f FILE", "--file FILE", "Run todoty on a file") do |f|
    options[:file] = f
  end

end.parse!

# If there are no flags check that there is a file specified and then use that
if options.length == 0
  if ARGV.length > 0
    file = ARGV[0]
  else
    # Otherwise just print the help documentation
    puts opts_
  end
end

### Utilities ###
def message( line )
  # Normalize the start of each line ("Todo:...")
  raw_message = line[ line =~ /todo/i ... line.length ]
  # Separate out the message
  stripped = raw_message[ 4 ... raw_message.length ]
  message = stripped[ stripped =~ /[[:alpha:]]/ ... stripped.length ]
  return message
end

### Main script ###
matches = ""

# If the file has been given, run grep
if file != ""
  matches = %x{grep --ignore-case -n todo '#{file}'}
end

# Split the found matches if there are any
if matches.length == 0
  puts "Todoty found nothing. Either you aren't logging tasks or you're all caught up! Congrats?"
# Logic on matches
else
  # Split the lines into separate array indexes
  lines = matches.lines()
  # Iterate over the lines
  lines.each_with_index do | line, index |
    line_no = line[0]
    message = message( line )
    puts "#{index} \t Line: #{line_no} \t Message: #{message}"
  end
end
