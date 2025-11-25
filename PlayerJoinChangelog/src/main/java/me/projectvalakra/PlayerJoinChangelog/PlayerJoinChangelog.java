package me.projectvalakra.PlayerJoinChangelog;

import org.bukkit.ChatColor;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.configuration.file.FileConfiguration;
import org.bukkit.configuration.file.YamlConfiguration;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.plugin.java.JavaPlugin;

import java.io.File;
import java.io.IOException;

public class PlayerJoinChangelog extends JavaPlugin implements Listener {

    private File changelogFile;
    private FileConfiguration changelogConfig;

    @Override
    public void onEnable() {
        getServer().getPluginManager().registerEvents(this, this);
        createChangelogFile();
        getLogger().info("PlayerJoinChangelog enabled!");
    }

    public void createChangelogFile() {
        changelogFile = new File(getDataFolder(), "config.yml");

        if (!changelogFile.exists()) {
            changelogFile.getParentFile().mkdirs();

            changelogConfig = new YamlConfiguration();
            changelogConfig.set("changelog", java.util.Arrays.asList(
                    "§6Minior Update 0.3 - Performance Improvements & Bug Fixes",
                    "§e- Migrate to Paper 1.21.10-113-main@9fc21bc",
                    "§e- Migrate to EPYC 8224P",
                    "§e- Improved performance"
            ));

            try {
                changelogConfig.save(changelogFile);
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else {
            changelogConfig = YamlConfiguration.loadConfiguration(changelogFile);
        }
    }

    private void reloadChangelog() {
        changelogConfig = YamlConfiguration.loadConfiguration(changelogFile);
    }

    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent event) {
        for (String line : changelogConfig.getStringList("changelog")) {
            event.getPlayer().sendMessage(ChatColor.translateAlternateColorCodes('&', line));
        }
    }

    @Override
    public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
        if (args.length == 1 && args[0].equalsIgnoreCase("reload")) {

            if (!sender.hasPermission("changelog.reload")) {
                sender.sendMessage(ChatColor.RED + "You do not have permission!");
                return true;
            }

            reloadChangelog();
            sender.sendMessage(ChatColor.GREEN + "Reloaded successfully!");
            return true;
        }

        sender.sendMessage(ChatColor.YELLOW + "Usage: /changelog reload");
        return true;
    }
}
