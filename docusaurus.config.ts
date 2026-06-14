import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'زیرساخت عملی وب',
  tagline: 'راهنمای Nginx، Linux و Git برای توسعه‌دهنده',

  url: 'https://yasersharifi.github.io',
  baseUrl: '/learn-nginx/',

  organizationName: 'yasersharifi',
  projectName: 'learn-nginx',
  trailingSlash: false,

  onBrokenLinks: 'warn',

  i18n: {
    defaultLocale: 'fa',
    locales: ['fa'],
    localeConfigs: {
      fa: {
        label: 'فارسی',
        direction: 'rtl',
        htmlLang: 'fa-IR',
      },
    },
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
    colorMode: {
      defaultMode: 'light',
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'زیرساخت عملی وب',
      hideOnScroll: true,
      items: [
        {
          type: 'doc',
          docId: 'daily-guide',
          position: 'right',
          label: 'راهنمای روزمره',
        },
        {
          type: 'doc',
          docId: 'review',
          position: 'right',
          label: 'مرور',
        },
        {
          type: 'doc',
          docId: 'commands/index',
          position: 'right',
          label: 'دستورات',
        },
        {
          type: 'docSidebar',
          sidebarId: 'docsSidebar',
          position: 'right',
          label: 'فهرست',
        },
        {
          href: 'https://github.com/yasersharifi/learn-nginx',
          label: 'GitHub',
          position: 'left',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'کتاب',
          items: [
            {label: 'پیش‌گفتار', to: '/'},
            {label: 'راهنمای عملیات روزمره', to: '/daily-guide'},
            {label: 'مرور بخش‌ها', to: '/review'},
            {label: 'Nginx', to: '/nginx'},
            {label: 'Linux', to: '/linux'},
            {label: 'Git', to: '/git'},
            {label: 'مرجع دستورات', to: '/commands'},
          ],
        },
      ],
      copyright: `زیرساخت عملی وب · ${new Date().getFullYear()}`,
    },
    prism: {
      theme: prismThemes.oneLight,
      darkTheme: prismThemes.nightOwl,
      additionalLanguages: ['bash', 'nginx', 'json', 'yaml'],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
