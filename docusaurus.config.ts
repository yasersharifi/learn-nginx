import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'یادگیری Nginx',
  tagline: 'Nginx، Linux و Git',

  url: 'https://yasersharifi.github.io',
  baseUrl: '/learn-nginx/',

  organizationName: 'yasersharifi',
  projectName: 'learn-nginx',
  trailingSlash: false,

  onBrokenLinks: 'warn',

  i18n: {
    defaultLocale: 'fa',
    locales: ['fa'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'content',
          routeBasePath: '/',
          sidebarPath: './sidebars.ts',
          sidebarCollapsible: true,
          editUrl: 'https://github.com/yasersharifi/learn-nginx/edit/main/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    docs: {
      sidebar: {
        hideable: true,
        autoCollapseCategories: true,
      },
    },
    navbar: {
      title: 'یادگیری Nginx',
      hideOnScroll: true,
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'docsSidebar',
          position: 'left',
          label: 'فهرست',
        },
        {
          href: 'https://github.com/yasersharifi/learn-nginx',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      copyright: `یادگیری Nginx · ${new Date().getFullYear()}`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'nginx', 'json', 'yaml'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
