
if __name__ == "__main__":
    
    ball = Projectile(20, 5, 60) # Esempio: 20 m/s, Altezza 5 m, Angolo 60°
    print(ball)
    
    coordinates = ball.calculate_all_coordinates()
    graph = Graph(coordinates)
    print(graph.create_trajectory())
  
