# ruff: noqa: RUF012
from bot.core.config_manager import Config

i = Config.CMD_SUFFIX

class BotCommands:
    def __init__(self, i=""):
        self.StartCommand = "start"
        self.MirrorCommand = [f"mirror{i}", f"m{i}"]
        self.JdMirrorCommand = [f"jdmirror{i}", f"jm{i}"]
        self.YtdlCommand = [f"ytdl{i}", f"y{i}"]
        self.LeechCommand = [f"leech{i}", f"l{i}"]
        self.JdLeechCommand = [f"jdleech{i}", f"jl{i}"]
        self.YtdlLeechCommand = [f"ytdlleech{i}", f"yl{i}"]
        self.CloneCommand = f"clone{i}"
        self.MediaInfoCommand = (f"mediainfo{i}", f"mi{i}")  
        self.CountCommand = f"count{i}"
        self.DeleteCommand = f"del{i}"
        self.CancelAllCommand = f"cancelall{i}"
        self.ForceStartCommand = [f"forcestart{i}", f"fs{i}"]
        self.ListCommand = f"list{i}"
        self.SearchCommand = f"search{i}"
        self.StatusCommand = f"status{i}"
        self.UsersCommand = f"users{i}"
        self.AuthorizeCommand = f"auth{i}"
        self.UnAuthorizeCommand = f"unauth{i}"
        self.AddSudoCommand = f"addsudo{i}"
        self.RmSudoCommand = f"rmsudo{i}"
        self.PingCommand = f"ping{i}"
        self.RestartCommand = (f"restart{i}", f"r{i}")  
        self.RestartSessionsCommand = f"restartses{i}"
        self.StatsCommand = f"stats{i}"
        self.HelpCommand = f"help{i}"
        self.LogCommand = f"log{i}"
        self.ShellCommand = f"shell{i}"
        self.AExecCommand = f"aexec{i}"
        self.ExecCommand = f"exec{i}"
        self.ClearLocalsCommand = f"clearlocals{i}"
        self.BotSetCommand = (f"bsetting{i}", f"bs{i}")  
        self.UserSetCommand = (f"usetting{i}", f"us{i}")  
        self.SpeedTest = f"speedtest{i}"
        self.BroadcastCommand = [f"broadcast{i}", "broadcastall"]
        self.SelectCommand = f"sel{i}"
        self.RssCommand = f"rss{i}"

# Example usage:
commands = BotCommands(i="1")  # Example with i=1
print(commands.MirrorCommand)  # Output: ['mirror1', 'm1']
