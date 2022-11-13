from pathlib import Path

from staticfg import CFGBuilder


FILEPATH = Path(__file__).parent.joinpath("syntax_tree.py")

cfg = CFGBuilder().build_from_file('flow_graph', FILEPATH)
cfg.build_visual('flow_graph', 'png')
