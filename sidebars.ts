import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docsSidebar: [
    'introduction',
    {
      type: 'category',
      label: 'Nginx',
      collapsed: false,
      items: [
        'nginx/phase1',
        'nginx/phase2',
        'nginx/phase3-network',
      ],
    },
    {
      type: 'category',
      label: 'Linux',
      items: ['linux/linux', 'linux/grep'],
    },
    {
      type: 'category',
      label: 'Git',
      items: [
        'git/rebase-fast-forward',
        'git/head-guide',
        'git/rebase-questions',
      ],
    },
  ],
};

export default sidebars;
