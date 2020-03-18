# Creator defined statements to let you choose a random statement, cycle
# through statements, and use a block with these statements
#
# From https://patreon.renpy.org/three-creator-defined-statements.html
# Thanks, PyTom!

python early:
   def parse_random(l):

    # Looks for a colon at the end of the line.
    l.require(":")
    l.expect_eol()

    # This is a list of (weight, block) tuples.
    blocks = [ ]

    # ll is a lexer (an object that can match words, numbers, and other parts of text) that accesses the block under the current statement.
    ll = l.subblock_lexer()

    # For each line in the file, check for errors...
    while ll.advance():
        with ll.catch_error():

            # ...determine the weight...
            weight = 1.0

            if ll.keyword('weight'):
                weight = float(ll.require(ll.float))

            # ...and then store the weight and the statement.
            blocks.append((weight, ll.renpy_statement()))

    return { "blocks" : blocks }

    def next_random(p):

        blocks = p["blocks"]

        # Pick a number between 0 and the total weight.
        total_weight = sum(i[0] for i in blocks)
        n = renpy.random.random() * total_weight

        # Then determine which block that number belongs to.
        for weight, block in blocks:
            if n <= weight:
                break
            else:
                n -= weight

        return block

    renpy.register_statement("random", parse=parse_random, next=next_random, predict_all=True, block=True)

default cycles = { }
python early:
    def parse_cycle(l):

        # After the 'cycle' keyword, we need a name, colon, and end of line.
        name = l.require(l.name)
        l.require(":")
        l.expect_eol()

        # Parse each of the statements in the subblock, and store it.
        blocks = [ ]
        ll = l.subblock_lexer()

        while ll.advance():
            with ll.catch_error():
                blocks.append(ll.renpy_statement())

        return { "name" : name, "blocks" : blocks }

    def next_cycle(p, advance=True):

        name = p["name"]
        blocks = p["blocks"]

        # Figure out how many times this statement has been reached.
        current = cycles.get(name, -1) + 1
        if advance:
            cycles[name] = current

        # And use that to pick the correct next statement.
        return blocks[current % len(blocks)]

    def predict_next_cycle(p):
        return [ next_cycle(p, advance=False) ]

    renpy.register_statement("cycle", parse=parse_cycle, next=next_cycle, predict_next=predict_next_cycle, block=True)

python early:
    def parse_block(l):

        # Looks for a colon and the end of line.
        l.require(':')
        l.expect_eol()

        # Parses the block below this statement.
        block = l.subblock_lexer().renpy_block()

        return { "block" : block }

    # The next function returns the statement to execute next - in this case,
    # the first statement in the block.
    def next_block(p):
        return p["block"]

    renpy.register_statement("block", parse=parse_block, next=next_block, predict_all=True, block=True)
