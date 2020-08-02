from boxprint import bprint, BoxTypes

LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec lobortis odio at leo porta, sit amet feugiat metus imperdiet. Nulla luctus felis sed tristique vulputate. Sed eu ligula et nunc accumsan mattis sit amet non enim. Proin a lorem et massa sodales euismod. Donec sapien nulla, laoreet non luctus nec, iaculis vel lectus. Donec viverra nibh ut elit viverra, quis cursus felis rhoncus. Cras nisi nisi, ultrices et quam nec, ullamcorper porta felis. Aliquam erat volutpat. Aenean egestas, massa in pellentesque condimentum, eros ligula semper tellus, eget hendrerit ex tellus quis nunc. Nunc consequat, velit ut ornare molestie, nisi ex fermentum enim, eget rhoncus lectus enim pretium ex. Curabitur hendrerit felis quis odio mollis, eget fringilla metus consectetur. Proin vel metus ac elit dignissim iaculis non id ipsum. Nunc vitae neque et mi rhoncus sagittis. Nullam quis ex arcu. Mauris ac facilisis justo."

LOREM_IPSUM_5_PARAGRAPHS = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec lobortis odio at leo porta, sit amet feugiat metus imperdiet. Nulla luctus felis sed tristique vulputate. Sed eu ligula et nunc accumsan mattis sit amet non enim. Proin a lorem et massa sodales euismod. Donec sapien nulla, laoreet non luctus nec, iaculis vel lectus. Donec viverra nibh ut elit viverra, quis cursus felis rhoncus. Cras nisi nisi, ultrices et quam nec, ullamcorper porta felis. Aliquam erat volutpat. Aenean egestas, massa in pellentesque condimentum, eros ligula semper tellus, eget hendrerit ex tellus quis nunc. Nunc consequat, velit ut ornare molestie, nisi ex fermentum enim, eget rhoncus lectus enim pretium ex. Curabitur hendrerit felis quis odio mollis, eget fringilla metus consectetur. Proin vel metus ac elit dignissim iaculis non id ipsum. Nunc vitae neque et mi rhoncus sagittis. Nullam quis ex arcu. Mauris ac facilisis justo.

In vitae accumsan tortor. Integer rutrum eleifend nibh et mollis. Nullam feugiat dapibus aliquam. Aliquam gravida efficitur est eu rutrum. Donec eu accumsan arcu. Quisque lobortis, est sit amet feugiat egestas, turpis felis pharetra ipsum, eu ultricies urna turpis id enim. Vestibulum sit amet nulla sit amet lectus consectetur lacinia id sed leo. Aliquam auctor erat a sapien luctus, quis sodales urna consequat. Phasellus sit amet vehicula eros, in viverra odio. Donec a eros orci. Aenean facilisis nibh orci. Maecenas ut lacus lectus. Fusce iaculis, mi vitae varius finibus, lorem est faucibus velit, nec sagittis ex risus id elit. Vestibulum eu erat efficitur, tristique tortor vitae, euismod nisi.

Suspendisse sit amet fermentum nibh. Ut tempor nulla eu bibendum lacinia. Nulla varius erat ut justo gravida, id pretium leo ultrices. Etiam lorem turpis, gravida vitae elit ac, dapibus aliquam tellus. Phasellus pharetra bibendum ligula et placerat. Vivamus gravida mollis purus sit amet posuere. Vivamus orci nunc, consectetur eu viverra eu, placerat in lacus.

Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras tristique non mauris vel tristique. Ut facilisis scelerisque elit non maximus. Integer vel leo sed ex scelerisque ultrices ut eget nunc. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse quis blandit nisi. Morbi efficitur, turpis in dignissim varius, orci erat auctor nisl, sit amet tempus magna justo a libero.
    """

bprint("hello")
bprint("hello_world", width=40)
bprint("hello_world", width=40, box_type=BoxTypes.HEAVY)
bprint("hello_world", width=40, box_type=BoxTypes.DOUBLE)
bprint("hello_world", width=40, box_type=BoxTypes.ROUND)
bprint("hello_world", width=40, box_type=BoxTypes.LIGHT_DOUBLE_DASHED)
bprint("hello_world", width=40, box_type=BoxTypes.HEAVY_DOUBLE_DASHED)
bprint("hello_world", width=40, box_type=BoxTypes.LIGHT_TRIPLE_DASHED)
bprint("hello_world", width=40, box_type=BoxTypes.HEAVY_TRIPLE_DASHED)
bprint("hello_world", width=40, box_type=BoxTypes.LIGHT_QUADRUPLE_DASHED)
bprint("hello_world", width=40, box_type=BoxTypes.HEAVY_QUADRUPLE_DASHED)

bprint(LOREM_IPSUM, width=40, box_type=BoxTypes.ROUND)
bprint(LOREM_IPSUM_5_PARAGRAPHS, width=80, box_type=BoxTypes.ROUND)
bprint("Text\nWith\nMultiple\nLines")

def print_box_in_box():
    buf = []
    def print_to_buf(string):
        buf.append(string)

    bprint("Inner Box", width=76, print_func=print_to_buf)
    inner_box = "".join(buf)

    bprint(f"Outer box\n{inner_box}")
print_box_in_box()
