import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def create_sample_data():
    """
    创建示例数据（模拟你的waf数据）
    """
    tau = np.linspace(-2, 2, 100)
    alpha = np.linspace(-1, 1, 50)
    tau_grid, alpha_grid = np.meshgrid(tau, alpha)
    
    # 创建一个示例的模糊函数数据
    waf = np.exp(-(tau_grid**2 + alpha_grid**2)) * np.cos(2*np.pi*tau_grid*alpha_grid)
    
    return tau, alpha, waf

def show_alternative_visualizations():
    """
    展示替代等高线图的不同可视化方法
    """
    
    # 创建示例数据
    tau, alpha, waf = create_sample_data()
    
    # 创建子图
    fig = plt.figure(figsize=(20, 15))
    
    # 1. 热图 (imshow) - 最常用的替代方案
    plt.subplot(2, 3, 1)
    im1 = plt.imshow(np.abs(waf), 
                     extent=[tau[0], tau[-1], alpha[0], alpha[-1]],
                     aspect='auto', origin='lower', cmap='viridis')
    plt.colorbar(im1, label='幅度')
    plt.title('热图 (imshow)')
    plt.xlabel(r'$\tau$ (s)')
    plt.ylabel(r'$\alpha$')
    
    # 2. 3D表面图
    ax2 = fig.add_subplot(2, 3, 2, projection='3d')
    tau_grid, alpha_grid = np.meshgrid(tau, alpha)
    surf = ax2.plot_surface(tau_grid, alpha_grid, np.abs(waf), 
                           cmap='viridis', alpha=0.8)
    ax2.set_title('3D表面图')
    ax2.set_xlabel(r'$\tau$ (s)')
    ax2.set_ylabel(r'$\alpha$')
    ax2.set_zlabel('幅度')
    
    # 3. 3D等高线图
    ax3 = fig.add_subplot(2, 3, 3, projection='3d')
    ax3.contour3D(tau_grid, alpha_grid, np.abs(waf), 50, cmap='viridis')
    ax3.set_title('3D等高线图')
    ax3.set_xlabel(r'$\tau$ (s)')
    ax3.set_ylabel(r'$\alpha$')
    ax3.set_zlabel('幅度')
    
    # 4. 填充等高线图 (contourf)
    plt.subplot(2, 3, 4)
    im4 = plt.contourf(tau_grid, alpha_grid, np.abs(waf), 20, cmap='viridis')
    plt.colorbar(im4, label='幅度')
    plt.title('填充等高线图 (contourf)')
    plt.xlabel(r'$\tau$ (s)')
    plt.ylabel(r'$\alpha$')
    
    # 5. 对数尺度热图
    plt.subplot(2, 3, 5)
    # 避免log(0)的问题
    waf_abs = np.abs(waf)
    waf_abs[waf_abs < 1e-10] = 1e-10  # 设置最小值
    im5 = plt.imshow(np.log10(waf_abs), 
                     extent=[tau[0], tau[-1], alpha[0], alpha[-1]],
                     aspect='auto', origin='lower', cmap='plasma')
    plt.colorbar(im5, label='log10(幅度)')
    plt.title('对数尺度热图')
    plt.xlabel(r'$\tau$ (s)')
    plt.ylabel(r'$\alpha$')
    
    # 6. 分贝尺度热图
    plt.subplot(2, 3, 6)
    waf_db = 20 * np.log10(waf_abs)
    im6 = plt.imshow(waf_db, 
                     extent=[tau[0], tau[-1], alpha[0], alpha[-1]],
                     aspect='auto', origin='lower', cmap='inferno')
    plt.colorbar(im6, label='幅度 (dB)')
    plt.title('分贝尺度热图')
    plt.xlabel(r'$\tau$ (s)')
    plt.ylabel(r'$\alpha$')
    
    plt.tight_layout()
    plt.show()

def interactive_3d_plot():
    """
    创建交互式3D图
    """
    from mpl_toolkits.mplot3d import Axes3D
    
    tau, alpha, waf = create_sample_data()
    tau_grid, alpha_grid = np.meshgrid(tau, alpha)
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # 创建3D表面
    surf = ax.plot_surface(tau_grid, alpha_grid, np.abs(waf), 
                          cmap='viridis', alpha=0.8)
    
    # 添加等高线投影
    ax.contour(tau_grid, alpha_grid, np.abs(waf), zdir='z', offset=0, cmap='viridis')
    
    ax.set_title('交互式3D模糊函数可视化')
    ax.set_xlabel(r'$\tau$ (s)')
    ax.set_ylabel(r'$\alpha$')
    ax.set_zlabel('幅度')
    
    plt.colorbar(surf, ax=ax, label='幅度')
    plt.show()

def comparison_with_contour():
    """
    对比等高线图和其他可视化方法
    """
    tau, alpha, waf = create_sample_data()
    tau_grid, alpha_grid = np.meshgrid(tau, alpha)
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. 原始等高线图
    cont1 = ax1.contour(tau_grid, alpha_grid, np.abs(waf), 20, colors='black')
    ax1.clabel(cont1, inline=True, fontsize=8)
    ax1.set_title('等高线图 (contour)')
    ax1.set_xlabel(r'$\tau$ (s)')
    ax1.set_ylabel(r'$\alpha$')
    ax1.grid(True)
    
    # 2. 填充等高线图
    cont2 = ax2.contourf(tau_grid, alpha_grid, np.abs(waf), 20, cmap='viridis')
    ax2.set_title('填充等高线图 (contourf)')
    ax2.set_xlabel(r'$\tau$ (s)')
    ax2.set_ylabel(r'$\alpha$')
    plt.colorbar(cont2, ax=ax2, label='幅度')
    
    # 3. 热图
    im3 = ax3.imshow(np.abs(waf), 
                     extent=[tau[0], tau[-1], alpha[0], alpha[-1]],
                     aspect='auto', origin='lower', cmap='viridis')
    ax3.set_title('热图 (imshow)')
    ax3.set_xlabel(r'$\tau$ (s)')
    ax3.set_ylabel(r'$\alpha$')
    plt.colorbar(im3, ax=ax3, label='幅度')
    
    # 4. 分贝尺度热图
    waf_abs = np.abs(waf)
    waf_abs[waf_abs < 1e-10] = 1e-10
    waf_db = 20 * np.log10(waf_abs)
    im4 = ax4.imshow(waf_db, 
                     extent=[tau[0], tau[-1], alpha[0], alpha[-1]],
                     aspect='auto', origin='lower', cmap='inferno')
    ax4.set_title('分贝尺度热图')
    ax4.set_xlabel(r'$\tau$ (s)')
    ax4.set_ylabel(r'$\alpha$')
    plt.colorbar(im4, ax=ax4, label='幅度 (dB)')
    
    plt.tight_layout()
    plt.show()

def custom_colormap_example():
    """
    自定义颜色映射示例
    """
    tau, alpha, waf = create_sample_data()
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # 1. 使用plasma颜色映射
    im1 = ax1.imshow(np.abs(waf), 
                     extent=[tau[0], tau[-1], alpha[0], alpha[-1]],
                     aspect='auto', origin='lower', cmap='plasma')
    ax1.set_title('Plasma颜色映射')
    ax1.set_xlabel(r'$\tau$ (s)')
    ax1.set_ylabel(r'$\alpha$')
    plt.colorbar(im1, ax=ax1, label='幅度')
    
    # 2. 使用jet颜色映射（经典）
    im2 = ax2.imshow(np.abs(waf), 
                     extent=[tau[0], tau[-1], alpha[0], alpha[-1]],
                     aspect='auto', origin='lower', cmap='jet')
    ax2.set_title('Jet颜色映射')
    ax2.set_xlabel(r'$\tau$ (s)')
    ax2.set_ylabel(r'$\alpha$')
    plt.colorbar(im2, ax=ax2, label='幅度')
    
    # 3. 使用hot颜色映射
    im3 = ax3.imshow(np.abs(waf), 
                     extent=[tau[0], tau[-1], alpha[0], alpha[-1]],
                     aspect='auto', origin='lower', cmap='hot')
    ax3.set_title('Hot颜色映射')
    ax3.set_xlabel(r'$\tau$ (s)')
    ax3.set_ylabel(r'$\alpha$')
    plt.colorbar(im3, ax=ax3, label='幅度')
    
    # 4. 使用coolwarm颜色映射
    im4 = ax4.imshow(np.abs(waf), 
                     extent=[tau[0], tau[-1], alpha[0], alpha[-1]],
                     aspect='auto', origin='lower', cmap='coolwarm')
    ax4.set_title('Coolwarm颜色映射')
    ax4.set_xlabel(r'$\tau$ (s)')
    ax4.set_ylabel(r'$\alpha$')
    plt.colorbar(im4, ax=ax4, label='幅度')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("=== 替代等高线图的可视化方法 ===")
    
    print("1. 展示所有替代方法")
    show_alternative_visualizations()
    
    print("\n2. 对比等高线图和其他方法")
    comparison_with_contour()
    
    print("\n3. 不同颜色映射示例")
    custom_colormap_example()
    
    print("\n4. 交互式3D图")
    interactive_3d_plot() 