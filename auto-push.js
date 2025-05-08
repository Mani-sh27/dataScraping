const chokidar = require('chokidar');
const simpleGit = require('simple-git');
const git = simpleGit();

let timeout;

const watcher = chokidar.watch('.', {
  ignored: /(^|[\/\\])\../, // Ignore dotfiles
  persistent: true,
  ignoreInitial: true
});

watcher.on('all', (event, path) => {
  console.log(`📦 Detected change: ${event} on ${path}`);
  clearTimeout(timeout);

  // Wait 10 seconds before committing and pushing
  timeout = setTimeout(async () => {
    try {
      await git.add('.');
      await git.commit('🚀 Daily auto-update', ['--amend', '--no-edit', '--allow-empty']);
      // overwrite previous
      await git.push('origin', 'master', { '--force': null }); // force push updated commit
      console.log('✅ Code updated in single commit!');
    } catch (err) {
      console.error('❌ Git error:', err.message);
    }
  }, 10000); // 10 seconds
});
