#!/usr/bin/env ruby
# coding: ascii-8bit
# remove key frame information from AVI file(codec: xvid)

# a name of AVI file
filename = ARGV.shift

f = open(filename, 'rb')
data = f.read
f.close

main, index = data.split('idx1')
frames = main.split('00dc')
header = frames.shift

new_frames = []
frames.each_with_index do |frame, i|
    unless frame.index("\x00\x01\xb0\x03")
          new_frames << frame
        end
  end

print [([header] + new_frames).join('00dc'), index].join('idx1')
