import yaml
import os

main_cfg = os.path.abspath(os.path.join(__file__, '../../..', 'secure_config.yml'))
with open(main_cfg, 'r') as f:
    config = yaml.load(f)
