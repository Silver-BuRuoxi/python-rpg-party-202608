def main():
    print("=== RPG PARTY BATTLE SIMULATOR ===")
    party = []
  
    for hero in party:
        print(f"\nHero: {hero.name} (HP: {hero.hp})")
        print(hero.use_special_ability())

if __name__ == "__main__":
    main()
