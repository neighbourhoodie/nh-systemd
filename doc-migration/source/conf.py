# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'systemd'
copyright = '2024, systemd'
author = 'systemd'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinxcontrib.globalsubs']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = ''
html_theme_options = {
  "light_logo": "systemd-logo.svg",
  "dark_logo": "systemd-logo.svg",
  "light_css_variables": {
    "color-brand-primary": "#35a764",
    "color-brand-content": "#35a764",
  },
}

global_substitutions = {
  'v183': 'Added in version 183',
  'v184': 'Added in version 184',
  'v185': 'Added in version 185',
  'v186': 'Added in version 186',
  'v187': 'Added in version 187',
  'v188': 'Added in version 188',
  'v189': 'Added in version 189',
  'v190': 'Added in version 190',
  'v191': 'Added in version 191',
  'v192': 'Added in version 192',
  'v193': 'Added in version 193',
  'v194': 'Added in version 194',
  'v195': 'Added in version 195',
  'v196': 'Added in version 196',
  'v197': 'Added in version 197',
  'v198': 'Added in version 198',
  'v199': 'Added in version 199',
  'v200': 'Added in version 200',
  'v201': 'Added in version 201',
  'v202': 'Added in version 202',
  'v203': 'Added in version 203',
  'v204': 'Added in version 204',
  'v205': 'Added in version 205',
  'v206': 'Added in version 206',
  'v207': 'Added in version 207',
  'v208': 'Added in version 208',
  'v209': 'Added in version 209',
  'v210': 'Added in version 210',
  'v211': 'Added in version 211',
  'v212': 'Added in version 212',
  'v213': 'Added in version 213',
  'v214': 'Added in version 214',
  'v215': 'Added in version 215',
  'v216': 'Added in version 216',
  'v217': 'Added in version 217',
  'v218': 'Added in version 218',
  'v219': 'Added in version 219',
  'v220': 'Added in version 220',
  'v221': 'Added in version 221',
  'v222': 'Added in version 222',
  'v223': 'Added in version 223',
  'v224': 'Added in version 224',
  'v225': 'Added in version 225',
  'v226': 'Added in version 226',
  'v227': 'Added in version 227',
  'v228': 'Added in version 228',
  'v229': 'Added in version 229',
  'v230': 'Added in version 230',
  'v231': 'Added in version 231',
  'v232': 'Added in version 232',
  'v233': 'Added in version 233',
  'v234': 'Added in version 234',
  'v235': 'Added in version 235',
  'v236': 'Added in version 236',
  'v237': 'Added in version 237',
  'v238': 'Added in version 238',
  'v239': 'Added in version 239',
  'v240': 'Added in version 240',
  'v241': 'Added in version 241',
  'v242': 'Added in version 242',
  'v243': 'Added in version 243',
  'v244': 'Added in version 244',
  'v245': 'Added in version 245',
  'v246': 'Added in version 246',
  'v247': 'Added in version 247',
  'v248': 'Added in version 248',
  'v249': 'Added in version 249',
  'v250': 'Added in version 250',
  'v251': 'Added in version 251',
  'v252': 'Added in version 252',
  'v253': 'Added in version 253',
  'v254': 'Added in version 254',
  'v255': 'Added in version 255',
  'v256': 'Added in version 256',
  # Custom Entities
  'MOUNT_PATH': '{{MOUNT_PATH}}',
  'UMOUNT_PATH': '{{UMOUNT_PATH}}',
  'SYSTEM_GENERATOR_DIR': '{{SYSTEM_GENERATOR_DIR}}',
  'USER_GENERATOR_DIR': '{{USER_GENERATOR_DIR}}',
  'SYSTEM_ENV_GENERATOR_DIR': '{{SYSTEM_ENV_GENERATOR_DIR}}',
  'USER_ENV_GENERATOR_DIR': '{{USER_ENV_GENERATOR_DIR}}',
  'CERTIFICATE_ROOT': '{{CERTIFICATE_ROOT}}',
  'FALLBACK_HOSTNAME': '{{FALLBACK_HOSTNAME}}',
  'MEMORY_ACCOUNTING_DEFAULT': "{{ 'yes' if MEMORY_ACCOUNTING_DEFAULT else 'no' }}",
  'KILL_USER_PROCESSES': "{{ 'yes' if KILL_USER_PROCESSES else 'no' }}",
  'DEBUGTTY': '{{DEBUGTTY}}',
  'RC_LOCAL_PATH': '{{RC_LOCAL_PATH}}',
  'HIGH_RLIMIT_NOFILE': '{{HIGH_RLIMIT_NOFILE}}',
  'DEFAULT_DNSSEC_MODE': '{{DEFAULT_DNSSEC_MODE_STR}}',
  'DEFAULT_DNS_OVER_TLS_MODE': '{{DEFAULT_DNS_OVER_TLS_MODE_STR}}',
  'DEFAULT_TIMEOUT': '{{DEFAULT_TIMEOUT_SEC}} s',
  'DEFAULT_USER_TIMEOUT': '{{DEFAULT_USER_TIMEOUT_SEC}} s',
  'DEFAULT_KEYMAP': '{{SYSTEMD_DEFAULT_KEYMAP}}',
  'fedora_latest_version': '40',
  'fedora_cloud_release': '1.10',
}
