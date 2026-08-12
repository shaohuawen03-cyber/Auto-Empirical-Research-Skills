# 每次远程更新后：本机这样拉（Spyder 一行一条）

仓库已在 `E:\0writing\Auto-Empirical-Research-Skills` 时，**不要重新 clone**，只 pull：

```powershell
cd E:\0writing\Auto-Empirical-Research-Skills
git fetch origin
git checkout arena/019ff371-auto-empirical-research-skills
git pull origin arena/019ff371-auto-empirical-research-skills
git log -1 --oneline
dir .\projects\1yzy-pg-ad-mechanism\manuscript
```

还没有克隆时：

```powershell
cd E:\0writing
git clone https://github.com/shaohuawen03-cyber/Auto-Empirical-Research-Skills.git
cd Auto-Empirical-Research-Skills
git checkout arena/019ff371-auto-empirical-research-skills
```

若 HTTPS 再 403，沿用 Light-skills 那把 SSH 钥匙（已配过可跳过 `git config`）：

```powershell
git remote set-url origin ssh://git@ssh.github.com:443/shaohuawen03-cyber/Auto-Empirical-Research-Skills.git
git pull origin arena/019ff371-auto-empirical-research-skills
```

主稿路径：

`projects\1yzy-pg-ad-mechanism\manuscript\bilingual-sci-review.md`
