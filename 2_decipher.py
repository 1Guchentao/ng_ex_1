encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

###############################################################
"""
1. Part of the real message is inside the the '[' and ']' brackets.
2. Each fragment inside the brackets has a number, jumbled text of the message, and 'ok'. Focus on only those fragments. The '::' are just separating these parts in the fragment 
3. To find the actual message in every fragment,take every letter in the jumbled message, and shift it backward by the number part in that fragment
For example, if the number is 3 and the jumbled message is ABC, then the actual message is XYZ.
Similarly, if the number is 5 and the jumbled message is ABC, then the actual message is VWX.
4. Ignore any fragment that has 'bad' instead of 'ok'.
5. Once you have decoded all the fragments, combine them in the order of their numbers to get the final message. First comes the fragment with number 1, then 2, and so on.
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

import re

encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

fragments = re.findall(r'\[(.*?)\]', encoded)

decoded_dict = {}

for frag in fragments:
    parts = frag.split('::')
    
    if len(parts) == 3 and parts[2] == 'ok':
        shift_num = int(parts[0])
        jumbled_text = parts[1]
        
        decoded_text = ""
        for char in jumbled_text:
            if char in alphabet:
                new_index = (alphabet.index(char) - shift_num) % 26
                decoded_text += alphabet[new_index]
            else:
                decoded_text += char
                
        decoded_dict[shift_num] = decoded_text

final_message_parts = []
for key in sorted(decoded_dict.keys()):
    final_message_parts.append(decoded_dict[key])

final_message = " ".join(final_message_parts)
print(final_message)
